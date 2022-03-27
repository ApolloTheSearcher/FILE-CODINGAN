# fungsi range() memberikan deret bilangan dengan pola tertentu.
# contoh sederhana:
# range dengan 1 parameter n : membuat deret bilangan yang dimulai dari 0, sebanyak n bilangan.
for i in range(5):
    print(i)
# range dengan 2 parameter m dan n : membuat deret bilangan yang dimulai dari m, sebanyak n bilangan.
for j in range(1,10):
    print(j)
# range dengan 3 parameter m, n, dan s : membuat deret bilangan yang dimulai dari m, sebanyak n bilangan, dengan selisih s.
print([_ for _ in range(1,10,2)]) # [1, 3, 5, 7, 9]
  