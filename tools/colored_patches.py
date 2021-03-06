# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:27:06 2017

@author: cvpr
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

#prewitt_img_path = '../data/Imageset/prewitt_images/000022.bmp'        #path to gradient image
#saliency_img_path = '../data/Imageset/saliency_images/000022_HC.bmp'      #path to saliency image

prewitt_img_path = './973_prewitt/973_prewitt.png'
saliency_img_path = './973_silent/973_silent.png'

file_path = '../patches_weight.txt'

patch_gradient = []
patch_saliency = []
weight = []    
prewitt_img = cv2.imread(prewitt_img_path, 0)
saliency_img = cv2.imread(saliency_img_path, 0)
height = prewitt_img.shape[0]
width = prewitt_img.shape[1]

colored_img = np.zeros((height, width))

#calculate weigh
for m in range(height/32):
    for n in range(width/32):
        prewitt_img_crop = prewitt_img[m*32:(m+1)*32, n*32:(n+1)*32]
        saliency_img_crop = saliency_img[m*32:(m+1)*32, n*32:(n+1)*32]
        
        prewitt_sum = np.sum(prewitt_img_crop)/255
        patch_gradient.append(prewitt_sum)            
        
        saliency_sum = np.sum(saliency_img_crop)/255
        patch_saliency.append(saliency_sum)
        temp = prewitt_sum*0.6+saliency_sum*0.4
        
        colored_img[m*32:(m+1)*32, n*32:(n+1)*32] = temp       
        weight.append(temp)




#fig, ax = plt.subplots()
#im = ax.imshow(colored_img, vmin=min(weight), vmax=max(weight))
#fig.subplots_adjust(right=1.0)
##cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
#cbar_ax = fig.add_axes([1.0, 0.15, 0.05, 0.7])           #location of colorbar:(x,y,w,h) 
#fig.colorbar(im, cax=cbar_ax)                            #show colorbar
#plt.savefig('./colored_img.eps')
#plt.show()

fig, ax = plt.subplots()
im = ax.imshow(colored_img, vmin=min(weight), vmax=max(weight))
#fig.subplots_adjust(right=1.0)
#cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
#cbar_ax = ax.add_axes([1.0, 0.15, 0.05, 0.7])           #location of colorbar:(x,y,w,h) 
#ax = plt.gca()

#ax.set_xticks(np.linspace(48,width-16,width/64))
#ax.set_xticklabels(('2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'))
#ax.set_yticks(np.linspace(48,height-16,height/64))
#ax.set_yticklabels(('2', '4', '6', '8', '10', '12', '14', '16'))
cbar_ax = fig.add_axes([0.92, 0.156, 0.02, 0.689])
fig.colorbar(im, cax=cbar_ax)                             #show colorbar
#plt.savefig('./color_img.eps')
plt.show()
