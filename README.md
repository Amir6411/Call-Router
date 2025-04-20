# Call Router
A simple speech recognition-based call routing system using HMMs and MFCC features.  
Routes calls to departments like Sales, Support, and Billing based on spoken keywords.


## Features
- Offline speech recognition
- Keyword-based routing
- Designed for small vocabulary commands


## HMM + MFCC (Traditional Pipeline)

  ## Process:
    1) Preprocessing: Clean audio
    2) Feature Extraction: Use MFCCs (Mel-Frequency Cepstral Coefficients)
    3) Modeling: Train an HMM per keyword
    4) Decoding: Use Viterbi algorithm to find the best keyword match

## To Do
- Add audio processing
- Build routing logic
- Integrate with telephony system


## Tools:
    1) Python + python_speech_features or librosa for MFCCs
    2) hmmlearn or custom HMM code
