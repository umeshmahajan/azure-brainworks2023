disable_mlock = true
ui            = true
 
listener "tcp" {
  address     = "127.0.0.1:8200"
  tls_disable = "true"
}
 
storage "file" {
  path = "C:\\workspace\\software\\vault\\vault_1.16.0_windows_386\\data"
}