import "./globals.css";
import NavBar from "@/components/NavBar";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html>
      <body className="antialiased flex flex-row min-h-screen w-screen">
        <NavBar />
        <div className="w-full min-h-screen">{children}</div>
      </body>
    </html>
  );
}
