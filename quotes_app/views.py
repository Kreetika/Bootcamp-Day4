from django.shortcuts import render

# Create your views here.
def quote(a):
   q= ['You have to keep breaking your heart until it opens.','Self-love is the greatest medicine','Think out of the box','Believe in yourself','The struggle ends when the gratitude begins']
   d = {
       'quote':q
   }
   return render(a,'quotes_app/quote.html',d)

def feature_quote(b):
    f = 'You have to keep breaking your heart until it opens.'
    d = {
        'featured_quote':f
    }
    return render(b, 'quotes_app/featured_q.html',d)

