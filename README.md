# MongoDB SCRAM Brute Force

See the medium article for an explanation
[https://medium.com/@attempto/brute-force-mongodb-scram-authentication-20acb4599f74](https://medium.com/@attempto/brute-force-mongodb-scram-authentication-20acb4599f74).

```python
python3 mongo_scram_brute.py --username admin --client_nonce <CLIENT_NONCE> --client_proof <CLIENT_PROOF> --combined_nonce <COMBINED_NONCE> --salt SALT  --iteration_count ITER_COUNT  --mechanisms 'SCRAM-SHA-256' --password_file /home/kali/rockyou.txt
```
