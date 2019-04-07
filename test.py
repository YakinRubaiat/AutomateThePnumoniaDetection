from HeatmapGenerator import HeatmapG
from HeatmapGenerator1 import HeatmapGenerator

pathInputImage = 'test/X_ray.png'
pathOutputImage = 'test/heatmap.png'
pathModel = 'models/m-25012018-123527.pth.tar'

nnArchitecture = 'DENSE-NET-121'
nnClassCount = 14

transCrop = 224


####  HeatMap model
h1 = HeatmapG(pathModel, nnArchitecture, nnClassCount, transCrop)

### Prediction model
h2 = HeatmapGenerator(pathModel,nnArchitecture, nnClassCount, transCrop)


### Generate Heatmap
h1.generate(pathInputImage, pathOutputImage, transCrop)

### Generate Prediction
predTensor = h2.generate(pathInputImage, pathOutputImage, transCrop)

rpred = predTensor.cpu().data.numpy()[0]

print(['%.3f' % (elem*100) for elem in list(rpred)])