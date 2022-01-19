from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    #TOP画面を表示する関数
    print("index関数を使ってTOP画面を表示します！") 
    return render(request, 'blog/index.html')


class IndexView(TemplateView):
    #TOP画面を表示するクラス
    template_name = 'blog/index.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("IndexViewを使ってTOP画面を表示します！")
        return self.render_to_response(context)