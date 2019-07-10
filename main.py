import UI.MainMenu as menu
import UI.graphicate as graph
import UI.complex_tools as complex_tools
import traceback


if __name__ == "__main__":
    try:
        menu.init()
        # print complex_tools.complex_eval()
        # graph.graphicate(complex(3,4))
        exit(1)
    except Exception as e:
        traceback.print_exc()
        exit(0)
    