import streamlit as st

from src.rag.rag_pipeline import RAGPipeline


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    # page_title="Haven Hotel & Bistro",
    # page_icon="🏨",
    layout="wide"
)


# ============================================================
# LOAD RAG PIPELINE
# ============================================================

@st.cache_resource
def load_rag():
    return RAGPipeline(top_k=3)


rag = load_rag()


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🏨 Haven Hotel")
    st.caption("AI Guest Assistant")

    st.divider()

    st.subheader("Hotel Information")

    st.write(
        "I can help you with:"
    )

    st.markdown(
        """
        - 🛏️ Rooms & check-in
        - 🍽️ Restaurant & food
        - 🛎️ Room service
        - ✈️ Airport transfers
        - 📍 Directions
        - 📋 Hotel policies
        - 🏨 Facilities
        """
    )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🛎️ AI Receptionist")

# st.caption(
#     "Your virtual assistant for hotel information and guest services."
# )


# ============================================================
# WELCOME MESSAGE
# ============================================================

if not st.session_state.messages:

    st.info(
        "👋 Welcome! Ask me anything about the hotel, "
        "restaurant, services, facilities, or policies."
    )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ============================================================
# SAMPLE QUESTIONS
# ============================================================

if not st.session_state.messages:

    st.subheader("💡 Try asking")

    sample_questions = [
        "Can I order food to my room?",
        "Does the hotel provide airport transfers?",
        "What food is available for breakfast?",
        "How far is the hotel from the railway station?",
        "Does the hotel have a swimming pool?"
    ]

    for i in range(0, len(sample_questions), 2):

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                sample_questions[i],
                key=f"sample_{i}",
                use_container_width=True
            ):
                st.session_state.selected_question = sample_questions[i]
                st.rerun()

        if i + 1 < len(sample_questions):

            with col2:

                if st.button(
                    sample_questions[i + 1],
                    key=f"sample_{i + 1}",
                    use_container_width=True
                ):
                    st.session_state.selected_question = sample_questions[i + 1]
                    st.rerun()

# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask the receptionist anything..."
)


# ============================================================
# HANDLE SAMPLE QUESTION
# ============================================================

if st.session_state.selected_question:

    question = st.session_state.selected_question

    st.session_state.selected_question = None


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.write(question)


    # --------------------------------------------------------
    # AI RESPONSE
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Checking hotel information..."
        ):

            answer = rag.ask(question)

        st.write(answer)


    # --------------------------------------------------------
    # SAVE RESPONSE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

# st.caption(
#     "Haven Hotel & Bistro • AI Guest Assistant"
# )