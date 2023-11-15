# bookhut
## bookhut.ir
### Necessary items for project implementation

```bash
pip install django
pip install rest_framework
pip install ckeditor
pip install jalali_date
pip install drf_yasg2
pip install colorfield
pip install admin_interface
```

### In this project, the Telegram bot has been connected to the website


### Also, the Zarin Pal payment portal has been connected to this project


#### To connect Zarin Pal payment portal to your website, you must do the following

```python

email = ''
MERCHANT = 'your MERCHANT code'
# from .tasks import payment_completed
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "وبسایت کلبه کتاب"  # Required
# mobile = '09123456789'  # Optional
CallbackURL = 'https://akoroman.ir/verifyboy'  # Important: need to edit for realy server.


class send_req2(View):
    def get(self, request):
        us = User.objects.filter(phone=request.user).first()
        mobile = us.phone
        amount = self.request.session['eshtrak']['many']
        result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))


class verify2(View):
    def get(self, request):
        user = ssion.objects.filter(user=request.user).first()
        if request.GET.get('Status') == 'OK':
            amount = self.request.session['eshtrak']['many']
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
            if result.Status == 100:
                us = User.objects.filter(phone=request.user).first()
                buy.objects.create(user=us, roman_id=self.request.session['eshtrak']['title'],
                                   many=self.request.session['eshtrak']['many'])
                return render(request, "success.html", {"id": result.RefID})
            elif result.Status == 101:

                return render(request, "submited.html", {"status": result.Status})
            else:

                return render(request, "failed.html", {"status": result.Status})
        else:
            return render(request, "cancel.html")

```

#### You must register on Zarin Pal website and get your own MERCHANT code and paste it so that the project works properly for you.
