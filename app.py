import streamlit as st
from preprocessing import preprocess_code
from model import calculate_similarity

# Pre-defined leaked code
leaked_code = """
class Solution {
public:
    string getSmallestString(string s) {
        int n = s.size();
        
        vector<int> oddIndices, evenIndices;
        
        for (int i = 0; i < n; ++i) {
            if ((s[i] - '0') % 2 == 0) {
                evenIndices.push_back(i);
            } else {
                oddIndices.push_back(i);
            }
        }
        
        sort(evenIndices.begin(), evenIndices.end(), [&](int i, int j) {
            return s[i] < s[j];
        });
        sort(oddIndices.begin(), oddIndices.end(), [&](int i, int j) {
            return s[i] < s[j];
        });
        
        string result = s;
        for (int i = 0; i < evenIndices.size(); ++i) {
            result[evenIndices[i]] = s[evenIndices[i]];
        }
        for (int i = 0; i < oddIndices.size(); ++i) {
            result[oddIndices[i]] = s[oddIndices[i]];
        }
        
        for (int i = 0; i < n - 1; ++i) {
            if ((s[i] - '0') % 2 == (s[i + 1] - '0') % 2 && s[i] > s[i + 1]) {
                swap(result[i], result[i + 1]);
                break;
            }
        }
        
        return result;
    }
};
"""

# CSS for better styling
st.markdown("""
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .input-box {
        width: 90%;
        margin: 10px;
    }
    .result-box {
        text-align: center;
        margin-top: 20px;
    }
    .code-container {
        display: flex;
        width: 100%;
        margin-top: 20px;
    }
    .code-column {
        width: 50%;
        padding: 0 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and input area for user code
st.title("Code Plagiarism Detection")
st.write("Compare your code against a leaked solution and see the plagiarism percentage.")
user_code = st.text_area("Enter your code here:", height=200)

if st.button("Detect Plagiarism"):
    if user_code.strip() == "":
        st.error("Please enter your code.")
    else:
        preprocessed_leaked_code = preprocess_code(leaked_code)
        preprocessed_user_code = preprocess_code(user_code)
        
        similarity_score = calculate_similarity(preprocessed_leaked_code, preprocessed_user_code)
        similarity_percentage = similarity_score * 100
        
        # Display code comparison
        st.markdown("<h4>Code Comparison</h4>", unsafe_allow_html=True)
        st.markdown("<div class='code-container'>", unsafe_allow_html=True)
        
        # Display leaked code
        st.markdown("<div class='code-column'>", unsafe_allow_html=True)
        st.markdown("<h5>Leaked Code</h5>", unsafe_allow_html=True)
        st.code(leaked_code, language='cpp')
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display user code
        st.markdown("<div class='code-column'>", unsafe_allow_html=True)
        st.markdown("<h5>Your Code</h5>", unsafe_allow_html=True)
        st.code(user_code, language='cpp')
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display plagiarism similarity score
        st.markdown(f"""
            <div class="result-box">
                <h3>Plagiarism Similarity Score: {similarity_percentage:.2f}%</h3>
            </div>
            """, unsafe_allow_html=True)
