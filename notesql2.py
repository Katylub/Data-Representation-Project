from clientDao import clientDao

client1 = {
    'ClientID': 1,
    'Names': 'John',
    'Surname': 'Kennedy',
    'Price': 60,

}
client2 = {
    'ClientID': 2,
    'Names': 'Mary',
    'Surname': 'Smith',
    'Price': 60,

}
client3 = {
    'ClientID': 3,
    'Names': 'Louise',
    'Surname': 'See',
    'Price': 60,

}
client6 = {
    'ClientID': 6,
    'Names': 'Leo',
    'Surname': 'See',
    'Price': 60,

}


#returnValue = clientDao.create(client6)
#print(returnValue)

#returnValue = clientDao.getAll()
#print(returnValue)

#returnValue = clientDao.findById(client2['ClientID'])
#print("find By Id")
#print(returnValue)

#returnValue = clientDao.update(client2)
#print(returnValue)


#returnValue = clientDao.findById(client2['ClientID'])
#print(returnValue)

returnValue = clientDao.delete(client6['ClientID'])
print(returnValue)

#returnValue = clientDao.getAll()
#print(returnValue)