def push(**kwargs):
    # pushes an XCom without a specific target
    print(kwargs['ti'])
    return kwargs['ti']


print(push())
