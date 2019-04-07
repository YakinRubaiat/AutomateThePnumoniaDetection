from HeatmapGenerator import HeatmapG
from HeatmapGenerator1 import HeatmapGenerator

class Prediction():
    """
    
    Produce the prediction and Heatmap 

    """

    def __init__(self):

        self.pathInputImage = 'images/X_ray.png'
        self.pathOutputImage = 'images/heatmap.png'
        pathModel = 'models/m-25012018-123527.pth.tar'

        nnArchitecture = 'DENSE-NET-121'
        nnClassCount = 14

        self.transCrop = 224


        ####  HeatMap model
        self.h1 = HeatmapG(pathModel, nnArchitecture, nnClassCount, self.transCrop)

        ### Prediction model
        self.h2 = HeatmapGenerator(pathModel,nnArchitecture, nnClassCount, self.transCrop)

    def predict(self):
        ### Generate Heatmap
        self.h1.generate(self.pathInputImage, self.pathOutputImage, self.transCrop)

        ### Generate Prediction
        predTensor = self.h2.generate(self.pathInputImage, self.pathOutputImage, self.transCrop)

        rpred = predTensor.cpu().data.numpy()[0]

        return ['%.3f' % (elem*100) for elem in list(rpred)]