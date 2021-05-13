import random
from django.contrib import messages

from django.shortcuts import render

# Create your views here.
def random_lotto(request):
    if request.method == 'POST':
        num = request.POST.get('num', None)
        
        if num is not None and num is not "":
            num = int(num)
            lottos = []
            for i in range(0, num):
                lotto = random.sample(range(1, 46), 6)
                lotto.sort()
                print(lotto)
                lottos.append(lotto)
            return render(request, 'lotto/random_lotto.html', {'lottos':lottos})
        else:
            messages.success(request, '정상적인 숫자를 넣어주십쇼잉.')
    return render(request, 'lotto/random_lotto.html', {})