import os
from flask import Flask
from flask import render_template
import utils.utils as utils

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

util_obj = utils.Util()
with open(os.path.join(util_obj.lmon_path, "config", "backend_server_url"), "r") as f:
    backend_url=f.read().strip()


@app.route("/api/v1/get-machines/<string:date>",
           methods=['GET'])
def get_machines(date):
    machines = util_obj.get_machines(date)
    return {date:machines}


@app.route("/api/v1/get-cpu-usage/<string:date>/<string:machine_id>",
           methods=['GET'])
def get_cpu_usage(date, machine_id):
    cpu_usage_dict = util_obj.get_machine_data(date, machine_id, 'cpu')
    return {date:cpu_usage_dict}


@app.route("/api/v1/get-mem-usage/<string:date>/<string:machine_id>",
           methods=['GET'])
def get_mem_usage(date, machine_id):
    mem_usage_dict = util_obj.get_machine_data(date, machine_id, 'mem')
    return {date:mem_usage_dict}


@app.route("/api/v1/get-login-details/<string:date>/<string:machine_id>",
           methods=['GET'])
def get_login_details(date, machine_id):
    login_details_dict = util_obj.get_login_details(date, machine_id)
    return {date:login_details_dict}


@app.route("/api/v1/ping-test/<string:date>",
           methods=['GET'])
def get_ping_test(date):
    ping_test_dict = util_obj.get_ping_ssh_test(date, "ping")
    return {date:ping_test_dict}


@app.route("/api/v1/ssh-test/<string:date>",
           methods=['GET'])
def get_ssh_test(date):
    ssh_test_dict = util_obj.get_ping_ssh_test(date, "ssh")
    return {date:ssh_test_dict}


@app.route("/api/v1/live-ping-test/<string:machine_id>",
           methods=['GET'])
def get_live_ping_test(machine_id):
    ping_successful = util_obj.get_live_ping_test(machine_id)
    return {machine_id:ping_successful}


@app.route("/api/v1/live-ssh-test/<string:machine_id>",
           methods=['GET'])
def get_live_ssh_test(machine_id):
    ssh_successful = util_obj.get_live_ssh_test(machine_id)
    return {machine_id:ssh_successful}


@app.route("/api/v1/live-ssh-test-other-machines/<string:IP>/<string:username>/<string:password>",
           methods=['GET'])
def get_live_ssh_test_other_machines(IP, username, password):
    ssh_successful = util_obj.get_live_ssh_test_other_machines(IP, username, password)
    return {IP:ssh_successful}


@app.route("/api/v1/get-avg-cpu-ram/<string:start_date>/<string:end_date>",
           methods=['GET'])
def get_avgusage_stats(start_date, end_date):
    average_stats = util_obj.get_average_stats(start_date, end_date)
    return average_stats


@app.route("/")
def index():
    return render_template("index.html", backend_url=backend_url)
