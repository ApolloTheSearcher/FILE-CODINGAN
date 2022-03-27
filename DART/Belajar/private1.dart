class User {
  late String nama;
  late final String password;
  // Final itu fungsinya kayak const
  // Agar sebuah variable gak bisa di ganti setelah diisi pertama kali
  // Final bisa di gunakan di field biasa atau juga staic
  // Kalo final digabung sama late,
  User (String nama, this.password){
    this.nama = nama;
  }
}
