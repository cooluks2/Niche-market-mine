from django.shortcuts import render, get_object_or_404
from market.models import Market, Store, MarketAttachFile, StoreAttachFile
from django.views.generic import TemplateView, DetailView, View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from mysite.views import OwnerOnlyMixin
from django.http import FileResponse
import os
from django.conf import settings


class MarketDV(View):

    def get(self, request, *args, **kwargs):
        queryset3 = get_object_or_404(Market, pk=kwargs['pk'])
        ctx = {
            'market_detail': queryset3
        }
        return render(request, 'market/market.html', ctx)


class MarketCreateView(CreateView):
    model = Market
    template_name = 'market/market_form.html'
    # introduction 빠져서 임시적인 주석처리
    # fields = ['market_name', 'introduction', 'location']
    fields = ['market_name', 'location']

    def get_success_url(self):
        return reverse('market:market', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = MarketAttachFile(market=self.object, filename=file.name, size=file.size,
                                           content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response


class MarketUpdateView(UpdateView):
    model = Market
    fields = ['market_name', 'introduction', 'location']

    def get_success_url(self):
        return reverse('market:market', kwargs={'pk': self.object.pk})


class MarketDeleteView(DeleteView):
    model = Market
    success_url = reverse_lazy('market:home')


class StoreLV(ListView):
    model = Store

    def get(self, request, *args, **kwargs):
        queryset = Store.objects.filter(market_list_id=kwargs['pk'])
        ctx = {
            'stores': queryset,
            'market_fk': kwargs['pk']
        }
        return render(request, 'market/store_list.html', ctx)


class StoreDV(DetailView):
    model = Store
    template_name = 'market/store_detail.html'


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    template_name = 'market/store_form.html'
    fields = ['store_name', 'store_introduction', 'open_hour', 'close_hour', 'hour_information']
    success_url = reverse_lazy('market:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.market_list = Market.objects.get(pk=self.kwargs.get('fk'))
        # form.instance.modify_dt = timezone.now()  # 업데이트 시간 버그 문제
        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = StoreAttachFile(post=self.object, filename=file.name,
                                          size=file.size, content_type=file.content_type,
                                          upload_file=file)
            attach_file.save()
        return response

        # return super().form_valid(form)


class StoreUpdateView(OwnerOnlyMixin, UpdateView):
    model = Store
    fields = ['store_name', 'store_introduction', 'open_hour', 'close_hour', 'hour_information']
    success_url = reverse_lazy('market:home')


class StoreDeleteView(OwnerOnlyMixin, DeleteView):
    model = Store
    success_url = reverse_lazy('market:home')


def market_download(request, id):
    file = MarketAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
    return FileResponse(open(file_path, 'rb'))


def store_download(request, id):
    file = StoreAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
    return FileResponse(open(file_path, 'rb'))
