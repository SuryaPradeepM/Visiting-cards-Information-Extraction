# Visiting Cards Information Extraction

This repository contains code to run the information extraction module for extracting relevant entities like:
* Name
* Phone number
* Fax
* Address
* Company name
* Designation
* Website
* Company Logo

from Visiting/Business cards.

## Getting Started

This code is fully compatible and tested with python 3.5.6. If you already have a higher version of python installed, use `pyenv` to install python 3.5.6. More instructions to install python 3.5.6 can be found [here](https://realpython.com/intro-to-pyenv/). Once you have python 3.5.6 installed with pyenv, you should also have pip(PIP is a package manager for Python packages, or modules). 

Make sure to upgrade `pip` using `pip3 install --upgrade pip`


### Prerequisites

```bash
cd visting_card_IE
pip3 install -r requirements.txt
```

For the text detection model, I'm using [CTPN](https://github.com/eragonruan/text-detection-ctpn), you may need to clone this to reproduce the results.

### Instructions for running the code

```
python3 main.py --imgs <img_path or directory containing images in jpg or png format>
```
`main.py` will runs the `text detection` model, `OCR` model, `logo detection` model and `entity extraction` model and produces all the outputs in `results/` folder.

`main.py` takes in argument `imgs` where you can specify either the path of the high quality visiting card or the path to the directory which contains all the high quality visiting cards in `jpg` or `png` format. The script first copies all the specified image(s) to `input_images/` directory and produces the corresponding outputs in `results/` folder. **Note**: During each run the contents of `input_images/` and `results/` folder will be cleared.

eg:
 ```
python3 main.py --imgs 'data/006.jpg'
```
will produce the following files in `results/`:

* `006.jpg`                 - is an image showing the highlighted results of the text detection model
* `res_006.txt`             - is a text file containing bounding box co-ordinates
* `logo_006.jpg`            - is an image containing the detected logo
* `final_results_006.json`  - is a json file containing all the extracted entities


## sample results

The entity extraction results for `data/006.jpg` is:

Input:

Text Detection model outputs:


Logo Detection results:


Information Extraction results:
```json
{
    "address": "350 SERRA MALL, ROOM 170\nSTANFORD, CALIFORNIA 94305-9505", 
    "fax": ["6507231882"],
    "website": [],
    "name": "RAFAEL ULATE",
    "designation": "DIRECTOR OF ADMISSIONS",
    "company": "STANFORD UNIVERSITY",
    "email": ["ulate@ee.stanford.edu"],
    "phone": ["6507259327", "9430595"]
}
```

The image results for the same file can be found in `sample_results/` folder


## Code hierarchy

```
./visiting_card_IE              : main folder
├── analyze_OCR.py              : Script to analyze and score entities in the OCRed Text
├── contour_detection.py        : Script to extract biggest contour in the image(used for logo detection)
├── data                        : folder containg sample data of visiting cards
├── helper.py                   : contains useful regexes and keywords for rule based entity extraction
├── input_images                : temporarily copies and stores the images the user has input for entity detection
├── main.py                     : Runs all the models and saves results
├── README.md                   : Instructions for building env, running code, etc
├── requirements.txt            : the libraries required to run/reproduce the results
├── results                     : temporarily stores the results(cleared after each run of `main.py`)
├── sample_results              : sample results
│   ├── 006.jpg
│   ├── final_results_006.json
│   ├── logo_006.png
│   └── res_006.txt
├── text-detection-model        : stores the text detection model scripts
└── utils.py                    : Useful utility functions

```