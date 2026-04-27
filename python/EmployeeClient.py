from __future__ import print_function
import logging

import grpc
import EmployeeService_pb2
import EmployeeService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = EmployeeService_pb2_grpc.EmployeeServiceStub(channel)

        # Query an employee's data
        response = stub.GetEmployeeDataFromID(EmployeeService_pb2.EmployeeID(id=101))
        print ('Employee\'s data: ' + str(response))

        # Add a new employee
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=301, name='Jose da Silva', title='Programmer'))
        print ('Added new employee ' + response.status)

        # Change an employee's title
        response = stub.UpdateEmployeeTitle(EmployeeService_pb2.EmployeeTitleUpdate(id=301, title='Senior Programmer'))
        print ('Updated employee ' + response.status)

        # Delete an employee
        response = stub.DeleteEmployee(EmployeeService_pb2.EmployeeID(id=201))
        print ('Deleted employee ' + response.status)

        # List all employees
        response = stub.ListAllEmployees(EmployeeService_pb2.EmptyMessage())
        print ('All employees: ' + str(response))

        # atualizar o nome do funcionario
        response = stub.UpdateEmployeeName(EmployeeService_pb2.EmployeeNameUpdate(id=101, name='Saravanan Kumar'))
        print ('Updated employee name ' + response.status)

        # get todos os funcionarios com um certo cargo
        response = stub.GetEmployeesByTitle(EmployeeService_pb2.EmployeeTitleFilter(title='Technical Leader'))
        print ('Employees with title Technical Leader: ' + str(response))

        # get o total de funcionarios
        response = stub.GetEmployeeCount(EmployeeService_pb2.EmptyMessage())
        print ('Total employees: ' + str(response.count))

if __name__ == '__main__':
    logging.basicConfig()
    run()
