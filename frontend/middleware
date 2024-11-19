import { NextResponse } from "next/server";
import { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const token = request.cookies.get("token"); // Recupera o token do cookie

  // Verifica se a rota atual é a de login
  const isLoginPage = request.nextUrl.pathname === "/login";

  // Se não estiver na página de login e não houver token
  if (!isLoginPage && !token) {
    return NextResponse.redirect(new URL("/login", request.url)); // Redireciona para a página de login
  }

  return NextResponse.next(); // Permite a requisição prosseguir
}

// Configure o middleware para todas as rotas
export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"], // Protege todas as rotas, exceto as que começam com "api", "_next/static", etc.
};
