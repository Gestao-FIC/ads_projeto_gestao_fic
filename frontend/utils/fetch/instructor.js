import axios from "axios";

const API_URL = process.env.NEXT_PUBLIC_BACKEND_URL + "/instructor/";

// Listar professores
export const fetchTeachers = async () => {
  try {
    const response = await axios.get(`${API_URL}`);
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar professores:", error);
    throw error;
  }
};

// Criar professor
export const createTeacher = async (teacher) => {
  try {
    const response = await axios.post(`${API_URL}`, teacher, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Erro ao criar professor:", error);
    throw error;
  }
};

// Atualizar professor
export const updateTeacher = async (id, updatedTeacher) => {
  try {
    const response = await axios.put(`${API_URL}${id}/`, updatedTeacher, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Erro ao atualizar professor:", error);
    throw error;
  }
};

// Excluir professor
export const deleteTeacher = async (id) => {
  try {
    await axios.delete(`${API_URL}${id}/`);
    return "Professor excluído com sucesso";
  } catch (error) {
    console.error("Erro ao excluir professor:", error);
    throw error;
  }
};
