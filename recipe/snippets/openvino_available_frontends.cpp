#include <cstdlib>

#include <openvino/frontend/manager.hpp>

int main() {
    return ov::frontend::FrontEndManager().get_available_front_ends().size() == 7 ? EXIT_SUCCESS : EXIT_FAILURE;
}
