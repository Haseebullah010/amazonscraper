from django.shortcuts import render
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse 

# Create your views here
@csrf_exempt
def vaidilty(request):

    try :

            
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        #link = request.POST.get["link"]
        #coupn=request.POST.get["coupn"]

        # link = request.POST.get('link')
        # coupn=request.POST.get('coupn')
        link ="https://www.amazon.com/ZELLINNI-Manual-Juicer-Detachable-Restaurant/dp/B08C271D19/ref=sr_1_24?crid=2X330586S2P17&keywords=manual%2Bfruit%2Bjuicer&qid=1644331068&sprefix=manual%2Bfruit%2Bjuicer%2Caps%2C102&sr=8-24&th=1"
        coupn="YVH2CFXF"
        
        print(link)
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)


        try :
            driver.get(link)
            time.sleep(2)

            selct=driver.find_element_by_class_name("a-button.a-button-dropdown.aui-variation.a-fastclick-disable")
            selct.click()
            time.sleep(3)

            size = driver.find_element_by_class_name("a-dropdown-item.dropdownAvailable")
            size.click()
            time.sleep(3)

            print ("size selected")

            add_to_cart = driver.find_element_by_id("add-to-cart-button")
            add_to_cart.click()
            time.sleep(2)

            driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
            time.sleep(2)

            a_input=driver.find_element_by_name("proceedToRetailCheckout")
            a_input.click()
            time.sleep(2)

            try :
                emial=driver.find_element_by_name("email")
                emial.clear()
                emial.send_keys("haseeblove110@gmail.com")
                        
                con=driver.find_element_by_id("continue")
                con.click()
                time.sleep(2)

                pas=driver.find_element_by_name("password")
                pas.clear()
                pas.send_keys("AllahG_001")

                signin = driver.find_element_by_id("signInSubmit")
                signin.click()
                time.sleep(3)
                print ("in try after login befor try")
                
                try :
                    print ("in try after login")
                    proced=driver.find_element_by_class_name("a-button-inner")
                    proced.click()
                    time.sleep(3)
                    promo=driver.find_element_by_link_text("Enter a gift card, voucher or promotional code")
                    # promo=driver.find_element_by_id("pp-eZ8b06-86")
                    promo.click()
                    time.sleep(3)



                    prom=driver.find_element_by_name("ppw-claimCode")
                    prom.clear()
                    # prom.send_keys("abcs")
                    prom.send_keys(coupn)
                    time.sleep(3)


                    apply_promo=driver.find_element_by_name("ppw-claimCodeApplyPressed")
                    apply_promo.click()
                    time.sleep(5)

                    if "You successfully applied the promotional code to the order" in driver.page_source:
                        # apply_promo=driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")
                        # apply_promo.click()
                        # time.sleep(5)

                        # apply_promo=driver.find_element_by_class_name("a-input-text a-spacing-micro a-span12 ")
                        # apply_promo.clear()
                        # apply_promo.send_keys(coupn)
                        # time.sleep(5)

                        # appl=driver.find_element_by_class_name("a-declarative a-button-text")
                        # appl.click()
                        # time.sleep(3)

                        # if "discount applied" in driver.page_source:
                        #     print ("double verify")
                        context = {
                            'error': "false",
                            'value':"valid"
                        }
                        
                        return JsonResponse(context)

                    elif "Please enter a valid promotion code" in driver.page_source:
                        # print ("not valid")
                        # apply_promo=driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")
                        # apply_promo.click()
                        # time.sleep(5)


                        # apply_promo=driver.find_element_by_class_name("a-input-text a-spacing-micro a-span12 ")
                        # apply_promo.clear()
                        # apply_promo.send_keys(coupn)
                        # time.sleep(5)

                        # appl=driver.find_element_by_class_name("a-declarative a-button-text")
                        # appl.click()
                        # time.sleep(3)

                        # if "discount applied" in driver.page_source:
                        #     print ("verified by final page")

                        context = {
                            'error': "false",
                            'valid':"invalid"
                        }
                        return JsonResponse(context)
                    
                    elif "The promotional code you entered cannot be applied to your purchase" in driver.page_source:
                        print ("not valid")
                        context= {
                                'error':"fasle",
                                'value':"invalid",   
                            }
                        return JsonResponse(context)

                except:
                    apply_promo=driver.find_element_by_name("claimCode")
                    apply_promo.clear()
                    apply_promo.send_keys(coupn)
                    time.sleep(5)

                    appl=driver.find_element_by_xpath("//input[@value='Apply']")

                    # appl=driver.find_element_by_class_name("a-button a-spacing-micro")
                    appl.click()
                    time.sleep(5)

                    if "discount applied" in driver.page_source:
                        print ("verify")
                        context = {
                            'error': "false",
                            'value':"valid"
                        }
                        return JsonResponse(context)

                        
                    else :
                        context = {
                            'error': "false",
                            'value':"invalid"
                        }                        
                        return JsonResponse(context)

            except:
                
                context = {

                'error':"true",
                'value': "Invalid Credentials"

                }
                return JsonResponse(context)
        
        except:
            print ("in main except")
            driver.get(link)
            time.sleep(2)

            
            add_to_cart = driver.find_element_by_id("add-to-cart-button")
            add_to_cart.click()
            time.sleep(2)
            
            
            
            driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
            
            time.sleep(2)
        


            a_input=driver.find_element_by_name("proceedToRetailCheckout")
            a_input.click()
            time.sleep(2)

            try :
                emial=driver.find_element_by_name("email")
                emial.clear()
                emial.send_keys("haseeblove110@gmail.com")
                        
                con=driver.find_element_by_id("continue")
                con.click()
                time.sleep(2)

                pas=driver.find_element_by_name("password")
                pas.clear()
                pas.send_keys("AllahG_001")

                signin = driver.find_element_by_id("signInSubmit")
                signin.click()
                time.sleep(5)
                print ("in try after login befor try")

                try :
                    print ("in try after login after try")
                    
                    proced=driver.find_element_by_class_name("a-button-inner")
                    proced.click()
                    time.sleep(3)
                    promo=driver.find_element_by_link_text("Enter a gift card, voucher or promotional code")
                    # promo=driver.find_element_by_id("pp-eZ8b06-86")
                    promo.click()
                    time.sleep(3)



                    prom=driver.find_element_by_name("ppw-claimCode")
                    prom.clear()
                    # prom.send_keys("abcs")
                    prom.send_keys(coupn)
                    time.sleep(3)


                    apply_promo=driver.find_element_by_name("ppw-claimCodeApplyPressed")
                    apply_promo.click()
                    time.sleep(5)

                    if "You successfully applied the promotional code to the order" in driver.page_source:
                        # apply_promo=driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")
                        # apply_promo.click()
                        # time.sleep(5)

                        # apply_promo=driver.find_element_by_class_name("a-input-text a-spacing-micro a-span12 ")
                        # apply_promo.clear()
                        # apply_promo.send_keys(coupn)
                        # time.sleep(5)

                        # appl=driver.find_element_by_class_name("a-declarative a-button-text")
                        # appl.click()
                        # time.sleep(3)

                        # if "discount applied" in driver.page_source:
                        #     print ("double verify")
                        context = {
                            'error': "false",
                            'value':"valid"
                        }
                        
                        return JsonResponse(context)

                    elif "Please enter a valid promotion code" in driver.page_source:
                        # print ("not valid")
                        # apply_promo=driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")
                        # apply_promo.click()
                        # time.sleep(5)


                        # apply_promo=driver.find_element_by_class_name("a-input-text a-spacing-micro a-span12 ")
                        # apply_promo.clear()
                        # apply_promo.send_keys(coupn)
                        # time.sleep(5)

                        # appl=driver.find_element_by_class_name("a-declarative a-button-text")
                        # appl.click()
                        # time.sleep(3)

                        # if "discount applied" in driver.page_source:
                        #     print ("verified by final page")

                        context = {
                            'error': "false",
                            'value':"invalid"
                        }
                        return JsonResponse(context)

                    elif "The promotional code you entered cannot be applied to your purchase" in driver.page_source:
                        print ("not valid")
                        context= {
                                'error':"fasle",
                                'value':"invalid",   
                            }
                        return JsonResponse(context)

                except:
                    print ("in except of try")
                    time.sleep(15)
                    apply_promo=driver.find_element_by_name("claimCode")
                    apply_promo.clear()
                    apply_promo.send_keys(coupn)
                    time.sleep(5)

                    appl=driver.find_element_by_xpath("//input[@value='Apply']")

                    # appl=driver.find_element_by_class_name("a-button a-spacing-micro")
                    appl.click()
                    time.sleep(5)
                    if "discount applied" in driver.page_source:
                        print ("verify from discount applied")
                        context = {
                            'error': "false",
                            'value':"valid"
                        }
                        return JsonResponse(context)

                    else:
                        print("verify from redeem promotion")
                        context = {
                            'error': "false",
                            'value':"invalid"
                        }
                        return JsonResponse(context)                        
                    
            except Exception as e:
                print ("error",e)
                
                context = {

                'error':"true",
                'value': "Invalid Credentials"

                }
                return JsonResponse(context)
        




    except :

        context = {
            'error':"true",
            'value':"Invalid Arguments"
        }

        return JsonResponse(context)


    # link = request.GET.get('link','www.google.com')
    # coupn=request.GET.get('coupn','abc')

    
    # try:
    #     driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    #     driver.get(link)
    #     time.sleep(3)
    #     add_to_cart = driver.find_element_by_name("submit.add-to-cart")
    #     print('cart')
    #     add_to_cart.click()
    #     print ("cart pressed")
    #     time.sleep(3)
    #     print ("sleep over after cart")
    #     driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    #     print ("cart accessed")
    #     time.sleep(3)
    #     a_input=driver.find_element_by_class_name("a-button-input")
    #     # a_input=driver.find_element_by_name("proceedToRetailCheckout")
    #     print ("checkout")
    #     a_input.click()
    #     print('retail')
    #     time.sleep(3)
    #     driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=amazon_checkout_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fbuy%2Fsignin%2Fhandlers%2Fcontinue.html%3Fie%3DUTF8%26brandId%3D%26cartItemIds%3D%26eGCApp%3D%26hasWorkingJavascript%3D0%26isEGCOrder%3D0%26isFresh%3D%26oldCustomerId%3D0%26oldPurchaseId%3D%26preInitiateCustomerId%3D%26purchaseInProgress%3D%26ref_%3Dcart_signin_submit%26siteDesign%3D&pageId=amazon_checkout_us&showRmrMe=0&siteState=isRegularCheckout.1%7CIMBMsgs.%7CisRedirect.1&suppressSignInRadioButtons=0')
    #     time.sleep(3)
    #     print ("link accessed")
        
    #     emial=driver.find_element_by_name("email")
    #     print ("email searched")
    #     emial.clear()
    #     print ("email clear")

    #     emial.send_keys("haseebtarar72@gmail.com")
    #     print ("email send")

    #     con=driver.find_element_by_id("continue")
    #     print('email')
    #     con.click()
    #     time.sleep(3)
    #     pas=driver.find_element_by_name("password")
    #     pas.clear()
    #     pas.send_keys("Haseebullah@12")
    #     print('password')
    #     signin = driver.find_element_by_id("signInSubmit")
    #     signin.click()
    #     time.sleep(3)

    #     print('sign in')


    #     proced=driver.find_element_by_class_name("a-button-inner")
    #     proced.click()
    #     time.sleep(3)

            

    #     promo=driver.find_element_by_link_text("Enter a gift card, voucher or promotional code")
    #     promo.click()
    #     time.sleep(3)
    #     print('prompt')

    #     prom=driver.find_element_by_name("ppw-claimCode")
    #     prom.clear()
    #     prom.send_keys(coupn)
    #     time.sleep(3)
    #     print('claimcode')

    #     apply_promo=driver.find_element_by_name("ppw-claimCodeApplyPressed")
    #     apply_promo.click()
    #     time.sleep(3)

    #     if "You successfully applied the promotional code to the order" in driver.page_source:
    #         context= {
    #                 'error':"False",
    #                 'value':"valid",
    #                 'link':"https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"
    #                 }
    #         return JsonResponse(context)

    #     elif "Please enter a valid promotion code" in driver.page_source:
    #         print ("not valid")
    #         context= {
    #                 'error':"Fasle",
    #                 'value':"not valid",
    #                 'link':"https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"
    #             }

    #         return JsonResponse(context)


        # elif "The promotional code you entered cannot be applied to your purchase" in driver.page_source:
        #     print ("not valid")
        #     context= {
        #             'error':"Fasle",
        #             'value':"not valid",
        #             'link':"https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"
        #         }

        #     return JsonResponse(context)


    # except:
       
        # context = {
        #     'error':"True",
        #     'value':"error",
        #     'message':"invalid argument"
        # }
        # return JsonResponse(context)
        
    

# def base(request):

#     return render(request,"base.html")
