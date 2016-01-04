# example application to work with Hoverfly

# Setup

    pip install -r requirements.txt
    
    
## Get URLs

    python fetch.py --urls 1
    
## Fetch projects

    python fetch.py
    
### But what if Hoverfly is too fast and I can't see anything?

Add iterations:


    python fetch.py --iterations 50
    