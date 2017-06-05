### Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 10000.


### Answer

The first idea came to me is to create a loop to look for the right numbers in range [1,10000[. The following Python code illustrates my first idea:


```python
sum = 0;
max = 10000

for i in range(1,max):
	if i % 3 == 0 or i % 5 == 0:
		sum += i

print sum

```

This way takes us around 0.1s with the complexity of `O(n)`.

However, instead of testing all values in range [1,10000[, we can just find the last number in the series of multiples of 3 and 5, and do some little math to get the final sum, without creating any unnecessary loop.

Basically we have two arithmetic progressions of 3 and 5. For each, the sum of all values can be computed as:

`sum = (x_1 + x_n)*n/2`

where `x_1` and `x_n` is the first and last number of the series, and `n` is the total number in the series.

Now we come to the second method:

```python
sum = 0
max = 10000

end3 = 3*((max - 1) // 3)
end5 = 5*((max - 1) // 5)

nb3 = (end3 - 3)/3 + 1
nb5 = (end5 - 5)/5 + 1

sum = (3 + end3)*nb3/2 + (5 + end5)*nb5/2

print sum
```

It also took us around 0.1s to finish. But when the range becomes larger, we will see the difference. For example, if `max = int(1e7)`, it takes around 2.8s to finish, while Method 2 still needs 0.1s to do the job.






