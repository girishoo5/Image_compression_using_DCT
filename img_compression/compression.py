import cv2
import numpy as np
import math
from zigzag import*

def get_run_length_encoding(image):
    i = 0
    skip = 0
    stream = []    
    bitstream = ""
    image = image.astype(int)
    while i < image.shape[0]:
        if image[i] != 0:            
            stream.append((image[i],skip))
            bitstream = bitstream + str(image[i])+ " " +str(skip)+ " "
            skip = 0
        else:
            skip = skip + 1
        i = i + 1
    return bitstream

def abc(imge):
    print(imge)
# defining block size
    block_size = 8
    # Quantization Matrix 
    QUANTIZATION_MAT = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56],
                                 [14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],
                                 [49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]])
    # reading image in grayscale style
    img =cv2.imread(imge,cv2.IMREAD_GRAYSCALE )
    
    # get size of the image
    [h , w]= img.shape
    # No of blocks needed : Calculation
    height = h
    width = w
    h = np.float32(h) 
    w = np.float32(w) 
    nbh = math.ceil(h/block_size)
    nbh = np.int32(nbh)
    nbw = math.ceil(w/block_size)
    nbw = np.int32(nbw)
    # height  and width of padded image
    H =  block_size * nbh
    W =  block_size * nbw
    padded_img = np.zeros((H,W))
    padded_img[0:height,0:width] = img[0:height,0:width]       
    for i in range(nbh):
            # Compute start and end row index of the block
            row_ind_1 = i*block_size                
            row_ind_2 = row_ind_1+block_size
            for j in range(nbw):           
                # Compute start & end column index of the block
                col_ind_1 = j*block_size                       
                col_ind_2 = col_ind_1+block_size                        
                block = padded_img[ row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2 ]                     
                # apply 2D discrete cosine transform to the selected block                       
                DCT = cv2.dct(block)                    
                DCT_normalized = np.divide(DCT,QUANTIZATION_MAT).astype(int)                      
                # reorder DCT coefficients in zig zag order by calling zigzag function        
                reordered = zigzag(DCT_normalized)
                # reshape the reorderd array 
                reshaped= np.reshape(reordered, (block_size, block_size)) 
                # copy reshaped matrix into padded_img 
                padded_img[row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2] = reshaped                           
    arranged = padded_img.flatten()
    bitstream = get_run_length_encoding(arranged)
    # Two terms are assigned for size as well, semicolon denotes end of image to reciever
    bitstream = str(padded_img.shape[0]) + " " + str(padded_img.shape[1]) + " " + bitstream + ";"
    print(" compressing done")
    # Written to image.txt
    file1 = open("image.txt","w+")
    file1.write(bitstream)
    file1.close()
    cv2.waitKey(0)
    cv2.destroyAllWindows()




     
