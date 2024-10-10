import React from 'react';
import { FaUser, FaLock } from 'react-icons/fa'; // Importando os ícones

const Login = () => {
  return (
    <div className="flex h-screen">
      <div className="w-1/2 bg-purple-100 flex items-center justify-center overflow-hidden rounded-lg">
        <img
          src="/images/Lucas.jpg"
          alt="Ilustração de fábrica"
          className="w-full h-auto max-h-screen object-cover rounded-lg"
          style={{
            clipPath: 'polygon(20% 0%, 100% 10%, 80% 100%, 0% 90%)',
            transform: 'scale(1.1)',
          }}
        />
      </div>
      <div className="w-1/2 bg-gradient-to-r from-purple-200 to-indigo-300 flex flex-col justify-center px-12">
        <div className="max-w-sm mx-auto">
          <h1 className="text-3xl font-bold text-gray-700 mb-6">
            Bem-vindo de volta ao
          </h1>
          <h2 className="text-4xl font-bold text-gray-900 mb-12">SGSET</h2>

          {/* Formulário */}
          <form>
            <div className="mb-4 relative">
              <label className="block text-gray-700 text-sm mb-2" htmlFor="username">
                Usuário
              </label>
              <div className="flex items-center border rounded-lg bg-gray-100">
                <span className="px-3">
                  <FaUser className="text-gray-500" /> {/* Ícone do usuário */}
                </span>
                <input
                  type="text"
                  id="username"
                  className="w-full px-4 py-2 bg-transparent focus:outline-none focus:border-blue-500"
                  placeholder="Usuário"
                />
              </div>
            </div>

            <div className="mb-6 relative">
              <label className="block text-gray-700 text-sm mb-2" htmlFor="password">
                Senha
              </label>
              <div className="flex items-center border rounded-lg bg-gray-100">
                <span className="px-3">
                  <FaLock className="text-gray-500" /> {/* Ícone da senha */}
                </span>
                <input
                  type="password"
                  id="password"
                  className="w-full px-4 py-2 bg-transparent focus:outline-none focus:border-blue-500"
                  placeholder="Senha"
                />
              </div>
            </div>

            <div className="flex items-center justify-between mb-6">
              <label className="flex items-center text-gray-700">
                <input type="checkbox" className="mr-2" />
                Lembrar de mim
              </label>
              <a href="#" className="text-blue-500">Recuperar a senha?</a>
            </div>

            <button
              type="submit"
              className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition duration-300"
            >
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
