# business_card_finder
This repo contains the utilities to upload business card and find it using the name of person whenever it's needed

### Description
- Pretrained detection and recognizer model is used to detect word in business card
- On uploading image, [card_db](https://github.com/shubh-tiwari/business_card_finder/blob/main/card_db/card_db.json) gets updated. card_db contains all the words extracted from respective images
- To search a business card with a given name, it is matched with the extracted words from each image uploaded in past

### Sample outputs for OCR
Sample output can be found in folder below- <br />
[https://github.com/shubh-tiwari/business_card_finder/tree/main/output_images/ocr_outputs](https://github.com/shubh-tiwari/business_card_finder/tree/main/output_images/)

<img src="https://github.com/shubh-tiwari/business_card_finder/blob/main/output_images/ocr_outputs/4.png" width="400"/> <img src="https://github.com/shubh-tiwari/business_card_finder/blob/main/output_images/ocr_outputs/3.png" width="400"/>

### Sample outputs for finder
- Solution takes care of spelling mistakes, incomplete names and case mismatches
- Solution takes care of small capturing deformations <br/><br/>

<b>Case 1 :<b/> 'Chris' is searched and it is matched with card of 'CHRIS SALCEDO'  <br/><br/>
<img src="https://github.com/shubh-tiwari/business_card_finder/blob/main/output_images/finder_outputs/img1.png" width="400"/> <br/><br/> 
<b>Case 1 :<b/> 'Bnard' is searched and the closest match to this word is 'BERNARD' <br/><br/> 
<img src="https://github.com/shubh-tiwari/business_card_finder/blob/main/output_images/finder_outputs/img2.png" width="400"/> <br/><br/> 
<b>Case 1 :<b/> 'MAR' is searched and the closest match to this word is 'MARK' <br/><br/>
<img src="https://github.com/shubh-tiwari/business_card_finder/blob/main/output_images/finder_outputs/img3.png" width="400"/> <br/><br/> 
<b>Case 1 :<b/> 'Rafal' is searched and the closest match to this word is 'RAFAEL' <br/><br/>
<img src="https://github.com/shubh-tiwari/business_card_finder/blob/main/output_images/finder_outputs/img4.png" width="400"/> <br/><br/> 

### To do lists
- Extracting exact person names, company names and telephone numbers from extracted datasets
- Image correction for skewness and deformations

### Try out
Check this notebook - <br/>
[https://github.com/shubh-tiwari/business_card_finder/blob/main/notebooks/test_finder.ipynb](https://github.com/shubh-tiwari/business_card_finder/blob/main/notebooks/test_finder.ipynb)

### References
1. [https://github.com/mindee/doctr](https://github.com/mindee/doctr)
2. [https://github.com/maxbachmann/RapidFuzz](https://github.com/maxbachmann/RapidFuzz)
3. [Stanford business card dataset](https://web.cs.wpi.edu/~claypool/mmsys-dataset/2011/stanford/mvs_images/business_cards.html)
