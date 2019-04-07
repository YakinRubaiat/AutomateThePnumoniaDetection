from HeatmapGenerator import HeatmapG

pathInputImage = 'test/00009285_000.png'
pathOutputImage = 'test/heatmap.png'
pathModel = 'models/m-25012018-123527.pth.tar'

nnArchitecture = 'DENSE-NET-121'
nnClassCount = 14

transCrop = 224

h = HeatmapG(pathModel, nnArchitecture, nnClassCount, transCrop)
h.generate(pathInputImage, pathOutputImage, transCrop)