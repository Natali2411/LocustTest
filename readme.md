pip install -r requirements.txt
locust --locustfile=D:\Repositories\coreapiautomation\load_tests\locustfile\locustfile.py --web-host=127.0.0.1

locust -f D:\Repositories\coreapiautomation\load_tests\locustfile\locustfile.py --web-host=127.0.0.1


#######
locust -f D:\Repositories\coreapiautomation\load_tests\locustfile\locustfile.py --headless -u 1000 -r 100 --run-time 0h3m

locust -f D:\Repositories\coreapiautomation\load_tests\locustfile\locustfile.py --headless -u 10 -r 1 --run-time 0h1m --host=127.0.0.1



bokeh serve
python plotter.py