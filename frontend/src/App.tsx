import { useEffect, useState } from "react";

type Room = {
  id: number;
  number: string;
  floor: number;
  room_type: string;
  housekeeping_status: string;
};

export default function App() {
  const [rooms, setRooms] = useState<Room[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("/api/v1/rooms/")
      .then((r) => r.json())
      .then(setRooms)
      .catch(() => setError("Не вдалося з'єднатися з backend"));
  }, []);

  return (
    <main style={{ fontFamily: "sans-serif", padding: 24 }}>
      <h1>HotelFlow</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <p>Номерів у базі: {rooms.length}</p>
      <table>
        <thead>
          <tr><th>Номер</th><th>Поверх</th><th>Категорія</th><th>Статус</th></tr>
        </thead>
        <tbody>
          {rooms.map((r) => (
            <tr key={r.id}>
              <td>{r.number}</td><td>{r.floor}</td><td>{r.room_type}</td><td>{r.housekeeping_status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
