"""
Routes and views for the flask application.
"""
import os
import base64
import json
from PIL import Image as PILImage
from io import BytesIO
from img2table.document import Image

# from PIL import Image
import tempfile

from flask import Flask, Request, request, jsonify, send_file, abort
from ImagePreprocessingAPI import app

prefix = '/api'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        


def get_table_cell_coords_from_image(byte_array):
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.tiff') # Crear un archivo temporal para almacenar la imagen
    
    try:
        # image = PILImage.open(BytesIO(byte_array))    
        # image.save(temp_file)
        
        temp_file.write(byte_array)                  # Escribir los bytes en el archivo temporal
        temp_file.close()                            # Cerrar el archivo para asegurarnos de que los datos estén guardados
        
        temp_file_path = temp_file.name              # Obtener la ruta del archivo temporal
        
        img = Image(src=temp_file_path)                   # Instancia de la imagen a procesar
        img_tableCellCoordinates = img.extract_tables()            # identificacion de la tabla en la imagen
        
        return img_tableCellCoordinates
        
    finally:        
        os.unlink(temp_file.name)                    # Eliminar el archivo temporal



def extract_lines(bounding_box):
    horizontal_lines = []
    vertical_lines = []
    
    x1, x2, y1, y2 = bounding_box['x1'], bounding_box['x2'], bounding_box['y1'], bounding_box['y2']
    
    # Extraer líneas horizontales dentro del rectángulo
    for y in range(y1, y2 + 1):
        horizontal_lines.append({'start': {'x': x1, 'y': y}, 'end': {'x': x2, 'y': y}})
    
    # Extraer líneas verticales dentro del rectángulo
    for x in range(x1, x2 + 1):
        vertical_lines.append({'start': {'x': x, 'y': y1}, 'end': {'x': x, 'y': y2}})
    
    return horizontal_lines, vertical_lines


def create_400_json_error(mensaje):

    respuesta = {
        "codigo_error": 400,
        "mensaje": mensaje
    }

    return json.dumps(respuesta), 400



@app.route(f'{prefix}/test')
def test():
    # Verificar si la solicitud es válida
    if not Request.is_json:
        abort(400, 'La solicitud debe ser JSON')

    return jsonify({'mensaje': 'solicitud recibida y procesada'}), 200


@app.route(f'{prefix}/process_image', methods=['POST'])
def process_image():
    
    if 'ImageBytes' not in request.json:
        return create_400_json_error("Solicitud incorrecta. El campo 'ImageBytes' es obligatorio.")
    
    try:       

        image_string = request.json['ImageBytes']
        image_bytes = base64.b64decode(image_string)
        
        tableCellCoordinates = get_table_cell_coords_from_image(image_bytes)
        table_info_list = []
        
        for table in tableCellCoordinates:                
            
            main_Rectangle_Table = {                                # Obtener el rectángulo principal de la tabla
                "x": table.bbox.x1,
                "y": table.bbox.y1,
                "width": table.bbox.x2,
                "height": table.bbox.y2
            }       
            
            row_count = len(table.content.values()) - 1             # Obtiene la cantidad de filas
            horizontal_line_rectangles = [None] * row_count         # Inicializar la lista con posiciones vacías

            first_row = next(iter(table.content.values()))          # Obtiene la primera fila
            cell_count = len(first_row)  -1                         # Obtiene la cantidad de celdas en la primera fila
            vertical_line_rectangles = [None] * cell_count          # Inicializar la lista con posiciones vacías
            current_row = 0
            
            for row in table.content.values():            

                pointInitial = (0, 0)
                pointFinal = (0, 0)          
                currentColumn = 0

                for cell in row:
                    
                    if pointInitial[0] == 0 and pointInitial[1] == 0:
                        pointInitial = (cell.bbox.x1,cell.bbox.y2)
                        
                    pointFinal = (cell.bbox.x2,cell.bbox.y2)               

                    
                    if currentColumn < cell_count:
                        if vertical_line_rectangles[currentColumn] is None:
                            vertical_line_rectangles[currentColumn] = [(cell.bbox.x2, cell.bbox.y1), (cell.bbox.x2, cell.bbox.y2)]
                        else:
                            vertical_line_rectangles[currentColumn][0] = (min(vertical_line_rectangles[currentColumn][0][0], cell.bbox.x2), min(vertical_line_rectangles[currentColumn][0][1], cell.bbox.y1))
                            vertical_line_rectangles[currentColumn][1] = (max(vertical_line_rectangles[currentColumn][1][0], cell.bbox.x2), max(vertical_line_rectangles[currentColumn][1][1], cell.bbox.y2))
                    
                    currentColumn += 1
                
                if current_row < row_count:         
                    pointsLineHorizontal = [pointInitial, pointFinal]                             # Almacenar los puntos en una lista    
                    horizontal_line_rectangles[current_row] = pointsLineHorizontal
                
                current_row += 1            
   
            table_info = {
                "main_table_bbox"          : main_Rectangle_Table,
                "rectanglesLinesHorizontal": horizontal_line_rectangles,
                "rectanglesLinesVerticales": vertical_line_rectangles
            }
            table_info_list.append(table_info)    
        
        return jsonify({'tableCellCoordinates': table_info_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500    

