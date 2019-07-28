from sense_hat import SenseHat
sense = SenseHat()

characters = [
	a, b, c, d, e, f, g, h,
	i, j, k, l, m, n, o, p, 
	q, r, s, t, u, v, w, x, 
	y, z, A, B, C, D, E, F, 
	G, H, I, J, K, L, M, N, 
	O, P, Q, R, S, T, U, V, 
	W, X, Y, Z, 1, 2, 3, 4, 
	5, 6, 7, 8, 9, 0, !, ?
	]  

for character in characters:
	sense.show_letter(character, white)
	precede = False
	while (not precede):
		for event in sense.stick.get_events():
			if (event.direction == 'middle' and event.action == 'pressed'):
				precede = not precede
