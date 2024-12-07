# # import speedtest

# # # Create a Speedtest object
# # speed_test = speedtest.Speedtest()

# # # Fetch the best server
# # speed_test.get_best_server()

# # # Measure download speed
# # download_speed = speed_test.download() / 1_000_000  # Convert to Mbps
# # print(f"Download Speed: {download_speed:.2f} Mbps")

# # # Measure upload speed
# # upload_speed = speed_test.upload() / 1_000_000  # Convert to Mbps
# # print(f"Upload Speed: {upload_speed:.2f} Mbps")

# # # Check ping (latency)
# # ping = speed_test.results.ping
# # print(f"Ping: {ping:.2f} ms")



# # from abc import ABC, abstractclassmethod

# # class Animal(ABC):
# #     @abstractclassmethod
# #     def make_sound(self):
# #         pass
    
# # class Bird(Animal):
# #     def fly(self):
# #         print("flying")
        
# #     def make_sound(self):
# #         print("Chirp")

# # bird = Bird() 
# # bird.fly()
# # bird.make_sound()



# # thisdict = {
# #     "brand": "Ford",
# #     "model": "Mustang",
# #     "year": 1964
# # }
# # print(thisdict.get("brand"))



# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
