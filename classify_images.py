#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Neelakshi Choudhary
# DATE CREATED: 8/07/23                                 
# REVISED DATE: 9/07/23
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to the classifier labels,
    and adds the classifier label and the comparison of the labels to the results dictionary.
    Parameters:
        images_dir - The (full) path to the folder of images that are to be classified by the classifier function (string)
        results_dic - Results Dictionary with 'key' as image filename and 'value' as a List.
                      The list will contain the following items:
                      index 0 = pet image label (string)
                      --- where index 1 & index 2 are added by this function ---
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int) where 1 = match between pet image and classifier labels and 0 = no match between labels
        model - Indicates which CNN model architecture will be used by the classifier function to classify the pet images,
                values must be either: resnet, alexnet, vgg (string)
    """
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = classifier(images_dir+'/'+key, model)
        classifier_label = classifier_label.lower().strip()
        results_dic[key].extend([classifier_label, int(pet_label in classifier_label)])

    print(results_dic)
