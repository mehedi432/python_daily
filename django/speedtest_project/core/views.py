from django.shortcuts import render
import speedtest

st = speedtest.Speedtest()

def main(request):
    context = {
        'download': st.download,
        'upload': st.best
    }

    return render(request, 'core/index.html', context=context)
