# Runbook: tạo user `dream-agent-deploy` trên Lightsail (CHỈ server Balheh — Hero chốt 02/11)

Mục đích: agent deploy / khởi động lại app bằng tài khoản quyền hẹp, không dùng user của Hero hay `ubuntu`.
**Hero chạy (hoặc cho phép Sidekick chạy từng bước). Xong thì ghi vào Sổ cấp quyền.**

- Khoá riêng: `~/.secrets/lightsail/dream-agent-deploy` (Mac mini, quyền 600)
- Khoá công khai: `~/.secrets/lightsail/dream-agent-deploy.pub`
- Fingerprint: `SHA256:Gi6T1qr1dvC37phFDy7KActcAgCOJOM+ZsE2LVV2k0I` (ED25519)

## 1. Tạo user (đăng nhập server bằng user admin của Hero)
```bash
sudo adduser --disabled-password --gecos "" dream-agent-deploy
sudo install -d -m 700 -o dream-agent-deploy -g dream-agent-deploy /home/dream-agent-deploy/.ssh
echo '<NỘI DUNG FILE dream-agent-deploy.pub>' | sudo tee /home/dream-agent-deploy/.ssh/authorized_keys
sudo chown dream-agent-deploy: /home/dream-agent-deploy/.ssh/authorized_keys
sudo chmod 600 /home/dream-agent-deploy/.ssh/authorized_keys
```

## 2. Quyền sudo hẹp — chỉ đúng lệnh cần
`sudo visudo -f /etc/sudoers.d/dream-agent-deploy`, ghi (thay `<SERVICE>` bằng tên dịch vụ thật):
```
dream-agent-deploy ALL=(root) NOPASSWD: /usr/bin/systemctl restart <SERVICE>, /usr/bin/systemctl status <SERVICE>, /usr/bin/journalctl -u <SERVICE> *
```
- App chạy bằng Docker → chỉ cho đúng lệnh `docker compose -f <đường dẫn>/docker-compose.yml up -d | ps | logs`. **Không** thêm user vào nhóm `docker` (tương đương quyền root).
- Thư mục deploy: chỉ cấp quyền ghi thư mục app (vd. `/opt/<app>/releases`).

## 3. Kiểm tra
```bash
ssh -i ~/.secrets/lightsail/dream-agent-deploy dream-agent-deploy@<HOST> 'whoami; sudo -l'
```
Phải thấy đúng các lệnh ở bước 2, **không** có `(ALL) ALL`.

## 4. Thu hồi
```bash
sudo deluser --remove-home dream-agent-deploy && sudo rm /etc/sudoers.d/dream-agent-deploy
```
→ ghi Nhật ký trong Sổ cấp quyền.
