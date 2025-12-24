import subprocess

FEAT_EMOJI = "🎉"
FIX_EMOJI = "🔧"
DOCS_EMOJI = "📄"
REFACTOR_EMOJI = "✨"
STYLE_EMOJI = "🎀"
TEST_EMOJI = "✅"
CHORE_EMOJI = "🧼"
BUILD_EMOJI = "🧬"

def main():
    print("--- Welcome to git-commit-message-helper ---")
    print("[!] Select the type of commit:", f"1. {FEAT_EMOJI} feat", f"2. {FIX_EMOJI} fix", f"3. {DOCS_EMOJI} docs", f"4. {REFACTOR_EMOJI} refactor", f"5. {STYLE_EMOJI} style", f"6. {TEST_EMOJI} test", f"7. {CHORE_EMOJI} chore", f"8. {BUILD_EMOJI} build", sep="\n")
    
    chosen_type = int(input("Enter no: "))
    message = input("Enter your message: ")
    final_message = ""

    if chosen_type == 1:
        final_message = f"{FEAT_EMOJI} feat: {message}"
    elif chosen_type == 2:
        final_message = f"{FIX_EMOJI} fix: {message}"
    elif chosen_type == 3:
        final_message = f"{DOCS_EMOJI} docs: {message}"
    elif chosen_type == 4:
        final_message = f"{REFACTOR_EMOJI} refactor: {message}"
    elif chosen_type == 5:
        final_message = f"{STYLE_EMOJI} style: {message}"
    elif chosen_type == 6:
        final_message = f"{TEST_EMOJI} test: {message}"
    elif chosen_type == 7:
        final_message = f"{CHORE_EMOJI} chore: {message}"
    elif chosen_type == 8:
        final_message = f"{BUILD_EMOJI} build: {message}"
    
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", final_message])


if __name__ == "__main__":
    main()