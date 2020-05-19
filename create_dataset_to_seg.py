from pydarknet import Detector, Image
import cv2
import sys


def crop(img_path):
  
  net = Detector(bytes("configuration/full_416/yolov3_416.cfg", encoding="utf-8"), bytes("configuration/full_416/full-416-best.weights", encoding="utf-8"), 0, bytes("configuration/vant.data",encoding="utf-8"))

  img = cv2.imread(img_path)

  img2 = Image(img)

  results = net.detect(img2)

  # print(results)
  
  # coloque o valor do cont referente a ultima imagem + 1
  count = 84 
  #regulador de tamanho da imagem gerada 
  const = 100
  for cat, score, bounds in results:
      
      filename = "./cropped_imgs/img{}.jpg".format(count)
      
      x, y, w, h = bounds
      
      try:
        crop_img = img[int(y - const):int(y + const +h), int(x - const):int(x + const + w)]
      except:
        print("imagem não formada")
      else:
        cv2.imwrite(filename, crop_img)
        count = count + 1 
      
    print("finish")

if __name__ == "__main__":
  try:
    img_path = sys.argv[1]
  except:
    print('insira o path de uma imagem')
    exit() 
  finally:
    crop(img_path)

  