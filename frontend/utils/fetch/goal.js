import axios from "axios";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

// Listar metas
export const fetchGoals = async () => {
  try {
    const response = await axios.get(`${BACKEND_URL}/goals/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching goals:", error);
    throw error;
  }
};

// Criar meta
export const createGoal = async (goal) => {
  try {
    const response = await axios.post(`${BACKEND_URL}/goals/`, goal, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error creating goal:", error);
    throw error;
  }
};

// Atualizar meta
export const updateGoal = async (id, updatedGoal) => {
  try {
    const response = await axios.put(
      `${BACKEND_URL}/goals/${id}/`,
      updatedGoal,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error("Error updating goal:", error);
    throw error;
  }
};

// Excluir meta
export const deleteGoal = async (id) => {
  try {
    await axios.delete(`${BACKEND_URL}/goals/${id}/`);
    return "Goal deleted successfully";
  } catch (error) {
    console.error("Error deleting goal:", error);
    throw error;
  }
};
