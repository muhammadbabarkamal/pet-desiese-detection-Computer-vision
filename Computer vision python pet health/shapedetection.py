# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:32:22 2019

@author: Dell
"""

import subprocess
import sys


try:
    import cv2
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'opencv-python'])
    
try:
    import numpy as np
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'numpy'])
 
try:
    import pandas as pd
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'pandas'])

import pandas as pd
def shape_detect(path):
    glucose = pd.read_csv('data/Glucose.csv')
    glucose=glucose.to_numpy()
    blood = pd.read_csv('data/Blood.csv')
    blood=blood.to_numpy()
    bilirubin = pd.read_csv('data/Bilirubin.csv')
    bilirubin=bilirubin.to_numpy()
    ketones =pd.read_csv('data/Ketones.csv')
    ketones=ketones.to_numpy()
    leukocytes =pd.read_csv('data/Leukocytes.csv')
    leukocytes=leukocytes.to_numpy()
    nitrite=pd.read_csv('data/Nitrite.csv')
    nitrite=nitrite.to_numpy()
    ph=pd.read_csv('data/pH.csv')
    ph=ph.to_numpy()
    protein=pd.read_csv('data/Protein.csv')
    protein=protein.to_numpy()
    sg=pd.read_csv('data/SG.csv')
    sg=sg.to_numpy()
    urobilinogen=pd.read_csv('data/Urobilinogen.csv')
    urobilinogen=urobilinogen.to_numpy()
    imgb = cv2.imread(path)
    imgb = cv2.resize(imgb,(260,420))
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(260,420))
           
    _, threshold =cv2.threshold(img, 50,255, cv2.THRESH_BINARY)
    
    con, hierarchy  =cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
           
    lista=[]
    i=0
    for cnt in con:
        if(con[i].shape[0]>5 and con[i].shape[0]<13):
            lista.append((con[i][1])[0][0])
            cv2.drawContours(img, [cnt], 0, (0), 1)
    
        elif(con[i].shape[0]>38 and con[i].shape[0]<49):
            cv2.drawContours(img, [cnt], 0, (0), 1)
            print(con[i].shape[0])        
        i=i+1
        
    imagea=imgb[ 30:390, (min(lista)):(min(lista)+20)]
    
    new1= imagea
    
    
    li=[]
    new2=cv2.Canny(new1,0,120)
    
    new22=new2
    for i in range(len(new2)):
        for j in range(len(new2[i])):
            if (new2[i][j]>1):
                li.append([i])
                break
            break
    
    if(imagea[ ((li[0])[0])+5:,:].shape[0]>325):
        i1=imagea[ ((li[0])[0])+5:,:]
    else:
        i1=imagea[ ((li[0])[0])-9:,:]
    
    
    _,thresh2=cv2.threshold(i1, 50,255, cv2.THRESH_BINARY)
    
    
    arr=[]
    for i in range(thresh2.shape[0]):
        for j in range(thresh2.shape[1]):
            if(thresh2[i][j][0]== 0):
                arr.append(i)
                break
    
    index=int(arr[0]/5)
    
    
    
    
    
    if (index>22 and index<24):
        index=23
    start_index=index-5
    print(i1[start_index][5],i1[start_index+index][5],i1[start_index+index*2][5],i1[start_index+index*3][5],
          i1[start_index+index*4][5],i1[(start_index+index*5)+10][5],i1[(start_index+index*6)+10][4],i1[(start_index+index*7)+10][4],i1[(start_index+index*8)+10][4],
          i1[(start_index+index*9)+10][4])
    leukocytes_distances=[]
    for i in range(len(leukocytes)):
        #leukocytes_distances.append((i1[start_index][5][0]-leukocytes[i][0])+(i1[start_index][5][1]-leukocytes[i][1])+(i1[start_index][5][2]-leukocytes[i][2]))
        leukocytes_distances.append(abs(((i1[start_index][5][0]-leukocytes[i][0])+(i1[start_index][5][1]-leukocytes[i][1])+(i1[start_index][5][2]-leukocytes[i][2]))))
    
    nitrite_distances=[]
    for i in range(len(nitrite)):
        nitrite_distances.append(abs((i1[start_index+index][5][0]-nitrite[i][0])+(i1[start_index+index][5][1]-nitrite[i][1])+(i1[start_index+index][5][2]-nitrite[i][2])))
    
    urobilinogen_distances=[]
    for i in range(len(urobilinogen)):
       urobilinogen_distances.append(abs((i1[start_index+index*2][5][2]-urobilinogen[i][2])+(i1[start_index+index*2][5][1]-urobilinogen[i][1])+(i1[start_index+index*2][5][0]-urobilinogen[i][0])))
    
    
    protein_distances=[]
    for i in range(len(protein)):
        protein_distances.append(abs((i1[start_index+index*3][5][2]-protein[i][2])+(i1[start_index+index*3][5][1]-protein[i][1])+(i1[start_index+index*3][5][0]-protein[i][0])))
    
    
    ph_distances=[]
    for i in range(len(ph)):
        ph_distances.append(abs((i1[start_index+index*4][5][2]-ph[i][2])+(i1[start_index+index*4][5][1]-ph[i][1])+(i1[start_index+index*4][5][0]-ph[i][0])))
    
    
    blood_distances=[]
    for i in range(len(blood)):
        blood_distances.append(abs((i1[(start_index+index*5)+10][5][2]-blood[i][2])+(i1[(start_index+index*5)+10][5][1]-blood[i][1])+(i1[(start_index+index*5)+10][5][0]-blood[i][0])))
        
        
    sg_distances=[]
    for i in range(len(sg)):
        sg_distances.append(abs((i1[(start_index+index*6)+10][5][2]-sg[i][2])+(i1[(start_index+index*6)+10][5][1]-sg[i][1])+(i1[(start_index+index*6)+10][5][0]-sg[i][0])))
    
    
    ketones_distances=[]
    for i in range(len(ketones)):
        ketones_distances.append(abs((i1[(start_index+index*7)+10][5][2]-ketones[i][2])+(i1[(start_index+index*7)+10][5][1]-ketones[i][1])+(i1[(start_index+index*7)+10][5][0]-ketones[i][0])))
    
    
    bilirubin_distances=[]
    for i in range(len(bilirubin)):
        bilirubin_distances.append(abs((i1[(start_index+index*8)+10][5][2]-bilirubin[i][2])+(i1[(start_index+index*8)+10][5][1]-bilirubin[i][1])+(i1[(start_index+index*8)+10][5][0]-bilirubin[i][0])))
    
    
    glucose_distances=[]
    for i in range(len(glucose)):
        glucose_distances.append(abs((i1[(start_index+index*9)+10][5][2]-glucose[i][2])+(i1[(start_index+index*9)+10][5][1]-glucose[i][1])+(i1[(start_index+index*9)+10][5][0]-glucose[i][0])))
   
        
    glucose_index=glucose_distances.index(min(glucose_distances))
    glucose_results=glucose[glucose_index][4]+" Results: "+glucose[glucose_index][3]
    print(glucose_results)    
    protein_index=protein_distances.index(min(protein_distances))
    protein_results=protein[protein_index][4]+" Results: "+protein[protein_index][3]
    print(protein_results)    
    blood_index=blood_distances.index(min(blood_distances))
    blood_results=blood[blood_index][4]+" Results: "+blood[blood_index][3]
    print(blood_results)
    ph_index=ph_distances.index(min(ph_distances))
    ph_results=ph[ph_index][4]+" Results: "+ph[ph_index][3]  
    print(ph_results)    
    sg_index=sg_distances.index(min(sg_distances))
    sg_results=sg[sg_index][4]+" Results: "+sg[sg_index][3]
    print(sg_results)
    ketones_index=ketones_distances.index(min(ketones_distances))
    ketones_results=ketones[ketones_index][4]+ " Results: "+ketones[ketones_index][3]  
    print(ketones_results) 
    bilirubin_index=bilirubin_distances.index(min(bilirubin_distances))
    bilirubin_results=bilirubin[bilirubin_index][4]+" Results: "+ bilirubin[bilirubin_index][3]  
    print(bilirubin_results)      
    urobilinogen_index=urobilinogen_distances.index(min(urobilinogen_distances))  
    urobilinogen_results=urobilinogen[urobilinogen_index][4]+ " Results: "+urobilinogen[urobilinogen_index][3]   
    print(urobilinogen_results)   
    nitrite_index=nitrite_distances.index(min(nitrite_distances))  
    nitrite_results=nitrite[nitrite_index][4]+ " Results: "+nitrite[nitrite_index][3]
    print(nitrite_results)
    leukocytes_index=leukocytes_distances.index(min(leukocytes_distances))  
    leukocytes_results=leukocytes[leukocytes_index][4]+ " Results: "+leukocytes[leukocytes_index][3]
    print(leukocytes_results)
    
    
    
    
    
    i2=np.zeros((i1.shape[0],i1.shape[1]+370,i1.shape[2]),dtype=int)
    i2=i2.astype(np.uint8)
    
    i2[0:i1.shape[0],0:i1.shape[1],0:i1.shape[2]]=i1
    
    
    #       LEUKOCYTES
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,(start_index))
    fontScale              = 0.5
    fontColor              = (leukocytes[leukocytes_index][0],leukocytes[leukocytes_index][1],leukocytes[leukocytes_index][2])
    lineType               = 2
    
    cv2.putText(i2,leukocytes_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    
    
    
    #      NITRITE             
    nitrite  
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,(start_index+index))
    fontScale              = 0.5
    fontColor              = (nitrite[nitrite_index][0],nitrite[nitrite_index][1],nitrite[nitrite_index][2])
    lineType               = 2
    
    cv2.putText(i2,nitrite_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #      UROBILINOGEN             
    urobilinogen
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,(start_index+index*2))
    fontScale              = 0.5
    fontColor              = (urobilinogen[urobilinogen_index][0],urobilinogen[urobilinogen_index][1],urobilinogen[urobilinogen_index][2])
    lineType               = 2
    
    cv2.putText(i2,urobilinogen_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #      PROTEIN                     
    protein
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,(start_index+index*3))
    fontScale              = 0.5
    fontColor              = (protein[protein_index][0],protein[protein_index][1],protein[protein_index][2])
    lineType               = 2
    
    cv2.putText(i2,protein_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #        PH                 
    ph
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,(start_index+index*4))
    fontScale              = 0.5
    fontColor              = (ph[ph_index][0],ph[ph_index][1],ph[ph_index][2])
    lineType               = 2
    
    cv2.putText(i2,ph_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #       BLOOD               
    blood
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,((start_index+index*5)+10))
    fontScale              = 0.5
    fontColor              = (blood[blood_index][0],blood[blood_index][1],blood[blood_index][2])
    lineType               = 2
    
    cv2.putText(i2,blood_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #       S>G                 
    sg
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,((start_index+index*6)+10))
    fontScale              = 0.5
    fontColor              = (sg[sg_index][0],sg[sg_index][1],sg[sg_index][2])
    lineType               = 2
    
    cv2.putText(i2,sg_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #       KENTONES            
    ketones
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,((start_index+index*7)+10))
    fontScale              = 0.5
    fontColor              = (ketones[ketones_index][0],ketones[ketones_index][1],ketones[ketones_index][2])
    lineType               = 2
    
    cv2.putText(i2,ketones_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #       Bilirubin                
    bilirubin
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,( (start_index+index*8)+10 ))
    fontScale              = 0.5
    fontColor              = (bilirubin[bilirubin_index][0],bilirubin[bilirubin_index][1],bilirubin[bilirubin_index][2])
    lineType               = 2
    
    cv2.putText(i2,bilirubin_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    #       GLUCOSE                       
    glucose
    
    font                   = cv2.FONT_ITALIC
    bottomLeftCornerOfText = (30,((start_index+index*9)+10))
    fontScale              = 0.5
    fontColor              = (glucose[glucose_index][0],glucose[glucose_index][1],glucose[glucose_index][2])
    lineType               = 2
    
    cv2.putText(i2,glucose_results, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    
    cv2.imshow('finaLLLLLLY',i2)
    cv2.imwrite('detected.jpg',i2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

