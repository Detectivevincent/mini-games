function game()
	num = math.random(100)
	n = 0
	while n ~= num do
		print("guess number:")
		n = io.read("*number")
		if n < num then
			print("no, too low")
		elseif n > num then
			print("no, too much")
		end
	end
end

game()