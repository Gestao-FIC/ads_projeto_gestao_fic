import axios from "axios";

const API_URL = process.env.NEXT_PUBLIC_BACKEND_URL + "/course-class/course-classes/";

// Listar professores
export const fetchCourseClasses = async () => {
  try {
    const response = await axios.get(`${API_URL}`);
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar cursos:", error);
    throw error;
  }
};


