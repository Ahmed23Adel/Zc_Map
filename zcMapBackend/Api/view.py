from rest_framework.response import Response
from rest_framework.decorators import api_view
from AILogic import main

@api_view(['GET'])
def getData(request):
    #http://127.0.0.1:8000/?format=json&id=yasmine
    alg = request.GET["alg"]
    type1 = request.GET["type1"]
    type2 = request.GET["type2"]
    row1 = request.GET["row1"]
    col1 = request.GET["col1"]
    row2 = request.GET["row2"]
    col2 = request.GET["col2"]
    exec_time, alg_output, path_cost = main.run(alg, type1, type2, row1,col1, row2,col2)
    output  = {'exec_time':exec_time,'alg_output':alg_output,'path_cost':path_cost }
    return Response(output)