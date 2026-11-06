// Bảng việc của Hero — API trên Netlify (dữ liệu nằm trong Netlify Blobs, không nằm trong code).
// Biến môi trường (Netlify > Site configuration > Environment variables):
//   BV_PASSWORD  mật khẩu Hero dùng để mở trang
//   BV_TOKEN     chìa khoá riêng của Mac mini để đẩy dữ liệu / lấy phản hồi (để trong ~/.secrets/netlify/bang-viec.json)
import { getStore } from "@netlify/blobs";

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

const isHero = (req) => !!process.env.BV_PASSWORD && req.headers.get("x-bv-password") === process.env.BV_PASSWORD;
const isMac = (req) => !!process.env.BV_TOKEN && req.headers.get("authorization") === `Bearer ${process.env.BV_TOKEN}`;

export default async (req) => {
  const store = getStore("bang-viec");
  const path = new URL(req.url).pathname.replace(/^\/api\/?/, "");

  // Hero xem bảng
  if (path === "data" && req.method === "GET") {
    if (!isHero(req)) return json({ error: "sai mật khẩu" }, 401);
    const data = (await store.get("data", { type: "json" })) || { generated: null, items: [] };
    const ticks = (await store.get("phan-hoi", { type: "json" })) || [];
    return json({ ...data, pending: ticks });
  }
  // Mac đẩy bảng mới
  if (path === "data" && req.method === "PUT") {
    if (!isMac(req)) return json({ error: "không có quyền" }, 401);
    await store.setJSON("data", await req.json());
    return json({ ok: true });
  }
  // Hero tick / ghi chú trên trang
  if (path === "tick" && req.method === "POST") {
    if (!isHero(req)) return json({ error: "sai mật khẩu" }, 401);
    const b = await req.json();
    if (!b.du_an || !b.id || !["xong", "bo-tick"].includes(b.hanh_dong)) return json({ error: "thiếu dữ liệu" }, 400);
    const list = (await store.get("phan-hoi", { type: "json" })) || [];
    const rest = list.filter((t) => !(t.du_an === b.du_an && t.id === b.id));
    if (b.hanh_dong === "xong") rest.push({ du_an: b.du_an, id: b.id, ghi_chu: String(b.ghi_chu || "").slice(0, 300), at: new Date().toISOString() });
    await store.setJSON("phan-hoi", rest);
    return json({ ok: true, pending: rest });
  }
  // Mac lấy phản hồi của Hero
  if (path === "phan-hoi" && req.method === "GET") {
    if (!isMac(req)) return json({ error: "không có quyền" }, 401);
    return json((await store.get("phan-hoi", { type: "json" })) || []);
  }
  // Mac báo đã ghi vào STATUS.md -> xoá khỏi hàng chờ
  if (path === "phan-hoi" && req.method === "POST") {
    if (!isMac(req)) return json({ error: "không có quyền" }, 401);
    const { done = [] } = await req.json();
    const key = (t) => `${t.du_an}/${t.id}`;
    const doneSet = new Set(done.map(key));
    const list = (await store.get("phan-hoi", { type: "json" })) || [];
    await store.setJSON("phan-hoi", list.filter((t) => !doneSet.has(key(t))));
    return json({ ok: true });
  }
  return json({ error: "không tìm thấy" }, 404);
};

export const config = { path: "/api/*" };
