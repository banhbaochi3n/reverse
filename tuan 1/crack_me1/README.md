# crack_me1

Test sơ qua thì đây có vẻ là một chương trình nhập key và check key. <br>
![oh_no](image.png)

Mở chương trình trong IDA xem mã giả.<br>

Hàm main chương trình như sau: <br>
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Format[160]; // [esp+8h] [ebp-2C4h] BYREF
  char password; // [esp+A8h] [ebp-224h] BYREF
  char v6[299]; // [esp+A9h] [ebp-223h] BYREF
  char v7[200]; // [esp+1D4h] [ebp-F8h] BYREF
  void *v8; // [esp+29Ch] [ebp-30h]
  int v9; // [esp+2A0h] [ebp-2Ch]
  int v10; // [esp+2A4h] [ebp-28h]
  char *v11; // [esp+2A8h] [ebp-24h]
  int v12; // [esp+2ACh] [ebp-20h]
  char *v13; // [esp+2B0h] [ebp-1Ch]
  int v14; // [esp+2B4h] [ebp-18h]
  int v15; // [esp+2B8h] [ebp-14h]
  char *v16; // [esp+2BCh] [ebp-10h]
  char *p_password; // [esp+2C0h] [ebp-Ch]
  int i; // [esp+2C8h] [ebp-4h]

  password = 0;
  memset(v6, 0, sizeof(v6));
  v9 = 335;
  memset(v7, 0, sizeof(v7));
  strcpy(
    Format,
    "Do you remember the good old days?! I don't know how about you,but I don't. Please help me to recover my memory, it'"
    "s password protected, and that's sad :(\n");
  v8 = &unk_734BE8;
  print(Format);
  print("Enter password: ");
  scanf("%300[^\n]s", &password);
  p_password = &password;
  v13 = v6;
  p_password += strlen(p_password);
  v12 = ++p_password - v6;
  v14 = p_password - v6;
  v16 = &password;
  v11 = v6;
  v16 += strlen(v16);
  v10 = ++v16 - v6;
  if ( (unsigned int)(v16 - v6) >= 0x126 )
  {
    if ( sub_7311D0(&password) )
    {
      v15 = v14 / 3;
      for ( i = 0; i < v14; ++i )
        v7[i % v15] ^= v6[i - 1];
      for ( i = 0; i < v9; ++i )
        flag[i] ^= v7[i % v15];
      print("\n\nCongratulation! Here is your memo :> \n\n");
      print("%s", flag);
    }
    else
    {
      print("\nInvalid password\n");
    }
    getchar();
    getchar();
    return 0;
  }
  else
  {
    print("oh, no!");
    return 0;
  }
}
```

