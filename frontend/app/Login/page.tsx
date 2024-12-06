import React from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import Image from "next/image";
import Link from "next/link";

const Login = () => {
  return (
    <div className="flex h-screen">
      <div className="w-1/2 bg-slate-200 flex items-center justify-center overflow-hidden ">
        <Image
          src={"/images/Login.jpeg"}
          height={774}
          width={816}
          alt="Ilustração de fábrica"
          className="w-full h-screen max-h-screen object-cover"
          style={{
            borderRadius: "25% 10% 40% 0 ",
          }}
        />
      </div>
      <div className="w-1/2 bg-gradient-to-r from-slate-200 to-slate-400 flex flex-col justify-center px-16 py-8">
        <div className="max-w-md mx-auto">
          <div className="flex-1 text-center">
            <h1 className="text-4xl font-bold text-gray-700 mb-8">
              Bem-vindo de volta ao
            </h1>
            <h2 className="text-5xl font-bold text-gray-900 mb-16">SGSET</h2>
          </div>

          {/* Formulário */}
          <form className="">
            <div className="mt-8">
              <label className="text-lg">Usuário:</label>
              <Input
                type="text"
                id="username"
                className="w-full rounded-xl px-6 py-3 bg-white focus:outline-none focus:border-slate-600 text-lg"
                placeholder="Usuário"
              />
            </div>
            <div className="mt-8">
              <label className="text-lg">Senha:</label>
              <Input
                type="password"
                id="password"
                className="w-full rounded-xl px-6 py-3 bg-white focus:outline-none focus:border-slate-600 text-lg"
                placeholder="Senha"
              />
            </div>

            <div className="flex items-center justify-between mt-8">
              <a href="#" className="text-lg text-blue-500">
                Recuperar a senha?
              </a>
            </div>

            <Link href={"/"}>
              <Button
                type="submit"
                className="w-full text-white py-3 rounded-lg hover:bg-slate-600 transition duration-300 mt-8 text-lg"
              >
                Login
              </Button>
            </Link>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
