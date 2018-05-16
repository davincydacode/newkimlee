for loopCheck in cart_list:

			if loopCheck[0] != pname:

				cart_list.append(arr)
				usage="New Item"
				count = request.session['count3']
				count+=1
				request.session['count3'] = count
				request.session['jcart6'] = cart_list



				
				#count = request.session['count1']
				#count+=1
			else:
				usage = "Item Already exist"
				updatequantity = loopCheck[2] + 1
				loopCheck[2] = updatequantity
				count = request.session['count3']
				count+=1
				request.session['count3'] = count
				request.session['jcart6'] = cart_list


				values=[]
				content=[]
				for i in range(3):

					values.append(i)

					if cart_list[i][0] == pname:

						use = "Already"
						content.append(cart_list[i][0])

					else:

						use="NEW"

