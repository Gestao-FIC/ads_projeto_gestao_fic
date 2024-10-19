import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const loginUser = async (username: string, password: string) => {
  try {
    const response = await axios.post(`${API_URL}/login/`, {
      username,
      password,
    });
    console.log('Login bem-sucedido:', response.data);  // Exibe a resposta no console
    return response.data;
  } catch (error) {
    console.error('Erro na requisição:', error);
    throw error;
  }
};

