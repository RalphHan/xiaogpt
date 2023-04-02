import setproctitle
setproctitle.setproctitle("xiaogpt")
from xiaogpt.cli import main
import sys
sys.argv = [sys.argv[0], "--config", "xiao_config.json"]
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    main()
